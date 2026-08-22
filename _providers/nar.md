---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 59
  human_in_the_loop: 0
  name: Nar Agentic Access
  operation_count: 88
  slug: nar-agentic-access
  summary_line: 88 operations · 59 acting
api_count: 1
apis:
- description: The external surface of NAR's REALTORS M1 Gateway - the members-first engagement system that is the single source of truth for REALTOR member data across state and local associations. The published Sw
  name: REALTORS M1 Gateway External API
  slug: nar-m1-gateway-external-api
artifact_total: 7
collections:
- collection_type: open
  name: M1Gateway - External
  slug: open-nar-m1-gateway-external
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nar-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nar-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nar-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nar-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nar-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nar-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nar-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nar-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nar-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/nar-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nar-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nar-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.nar.realtor/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NationalAssociationOfRealtors
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/national-association-of-realtors
- group: company
  title: ''
  type: Blog
  url: https://www.nar.realtor/blogs
- group: company
  title: ''
  type: Newsroom
  url: https://www.nar.realtor/newsroom
- group: other
  title: ''
  type: Policy
  url: https://www.nar.realtor/handbook-on-multiple-listing-policy/operational-issues-section-12-real-estate-transaction-standards-rets-policy-statement-790
- group: other
  title: ''
  type: Policy
  url: https://www.nar.realtor/about-nar/policies/mls-policy/real-estate-transaction-standards-rets-web-api
- group: docs
  title: ''
  type: Documentation
  url: https://www.nar.realtor/real-estate-transaction-standards-rets
- group: other
  title: ''
  type: Research
  url: https://www.nar.realtor/research-and-statistics
- group: operate
  title: ''
  type: Support
  url: https://www.nar.realtor/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nar.realtor/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nar.realtor/privacy-policy
created: '2026-07-26'
description: 'The National Association of REALTORS (NAR) is the largest trade association in the United States, representing roughly one million members across residential and commercial real estate. NAR is the industry body that sits above the roughly 500 local Multiple Listing Services, and it is the reason the US residential market has a machine-readable contract at all: MLS Policy Statement 7.90 requires MLS organizations owned and operated by associations of REALTORS to implement the RESO Data Dictionary and the RESO Web API and to stay current within one year of each ratification, with compliance demonstrated through the RESO Certification Process. NAR mandates that standard rather than operating it - RESO is a separate organization, and the listing data behind every certified endpoint is licensed through MLS membership, an IDX or VOW agreement, a broker relationship, or a reseller. NAR itself holds no RESO certification and publishes no self-serve developer portal. Its own API surface
  is REALTORS M1, the members-first engagement system that replaces NRDS: the M1 Gateway External API is a live, HTTP-Basic-authenticated REST API over member, office, association and data-extract records, whose Swagger 2.0 definition and Postman collection NAR publishes openly on GitHub for external association management system vendors and NAR partners, but whose credentials NAR issues only under a partner relationship.'
image: https://avatars.githubusercontent.com/u/7168861?v=4
layout: provider
mcp_servers:
- description: ''
  name: nar-mcp.yml
  slug: nar-mcpyml
modified: '2026-07-26'
name: National Association of REALTORS
nav: Providers
network: true
overview: 'National Association of REALTORS publishes 1 API on the [APIs.io](https://apis.io/) network: REALTORS M1 Gateway External API. Tagged areas include Real Estate, United States, Industry Body, MLS, and RESO.


  National Association of REALTORS''s developer surface includes authentication, engineering blog, documentation, support, and 21 more developer resources.'
random_paper: 6
rate_limits:
- limit_count: 1
  name: Nar Rate Limits
  slug: nar-rate-limits
score:
  band: thin
  composite: 31.7
  delta: 0.3
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 35.0
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 23.7
  previous_composite: 31.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nar/refs/heads/main/screenshots/nar-2026-08-07T184628.png
security:
- kind: authentication
  name: Nar Authentication
  slug: nar-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Nar Domain Security
  slug: nar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nar
tags:
- Real Estate
- United States
- Industry Body
- MLS
- RESO
- Standards
- Membership
- Property Listings
- IDX
- PropTech
website: https://www.nar.realtor/
---
