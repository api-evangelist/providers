---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 59
  human_in_the_loop: 0
  name: Nar Agentic Access
  operation_count: 88
  slug: nar-agentic-access
  summary_line: 88 operations · 59 acting
api_count: 1
apis:
- description: The Association API from National Association of REALTORS — 3 operation(s) for association.
  name: National Association of REALTORS Association API
  slug: nar-association-api
- description: The DataExtractRequest API from National Association of REALTORS — 4 operation(s) for dataextractrequest.
  name: National Association of REALTORS Data Extract Request API
  slug: nar-dataextractrequest-api
- description: The DataExtractSchedule API from National Association of REALTORS — 4 operation(s) for dataextractschedule.
  name: National Association of REALTORS Data Extract Schedule API
  slug: nar-dataextractschedule-api
- description: The Member API from National Association of REALTORS — 11 operation(s) for member.
  name: National Association of REALTORS Member API
  slug: nar-member-api
- description: The MemberAddress API from National Association of REALTORS — 2 operation(s) for memberaddress.
  name: National Association of REALTORS Member Address API
  slug: nar-memberaddress-api
- description: The MemberCertification API from National Association of REALTORS — 2 operation(s) for membercertification.
  name: National Association of REALTORS Member Certification API
  slug: nar-membercertification-api
- description: The MemberCoe API from National Association of REALTORS — 2 operation(s) for membercoe.
  name: National Association of REALTORS Member Coe API
  slug: nar-membercoe-api
- description: The MemberDemographic API from National Association of REALTORS — 2 operation(s) for memberdemographic.
  name: National Association of REALTORS Member Demographic API
  slug: nar-memberdemographic-api
- description: The MemberDesignation API from National Association of REALTORS — 2 operation(s) for memberdesignation.
  name: National Association of REALTORS Member Designation API
  slug: nar-memberdesignation-api
- description: The MemberDuesPayment API from National Association of REALTORS — 2 operation(s) for memberduespayment.
  name: National Association of REALTORS Member Dues Payment API
  slug: nar-memberduespayment-api
- description: The MemberEducation API from National Association of REALTORS — 2 operation(s) for membereducation.
  name: National Association of REALTORS Member Education API
  slug: nar-membereducation-api
- description: The MemberEducationLevel API from National Association of REALTORS — 2 operation(s) for membereducationlevel.
  name: National Association of REALTORS Member Education Level API
  slug: nar-membereducationlevel-api
- description: The MemberEmail API from National Association of REALTORS — 2 operation(s) for memberemail.
  name: National Association of REALTORS Member Email API
  slug: nar-memberemail-api
- description: The MemberFairHousing API from National Association of REALTORS — 2 operation(s) for memberfairhousing.
  name: National Association of REALTORS Member Fair Housing API
  slug: nar-memberfairhousing-api
- description: The MemberFieldOfBusiness API from National Association of REALTORS — 2 operation(s) for memberfieldofbusiness.
  name: National Association of REALTORS Member Field Of Business API
  slug: nar-memberfieldofbusiness-api
- description: The MemberIscAffiliation API from National Association of REALTORS — 2 operation(s) for memberiscaffiliation.
  name: National Association of REALTORS Member Isc Affiliation API
  slug: nar-memberiscaffiliation-api
- description: The MemberLanguage API from National Association of REALTORS — 2 operation(s) for memberlanguage.
  name: National Association of REALTORS Member Language API
  slug: nar-memberlanguage-api
- description: The MemberMilitaryService API from National Association of REALTORS — 2 operation(s) for membermilitaryservice.
  name: National Association of REALTORS Member Military Service API
  slug: nar-membermilitaryservice-api
- description: The MemberMLS API from National Association of REALTORS — 2 operation(s) for membermls.
  name: National Association of REALTORS Member MLS API
  slug: nar-membermls-api
- description: The MemberPhone API from National Association of REALTORS — 2 operation(s) for memberphone.
  name: National Association of REALTORS Member Phone API
  slug: nar-memberphone-api
- description: The MemberSecondary API from National Association of REALTORS — 2 operation(s) for membersecondary.
  name: National Association of REALTORS Member Secondary API
  slug: nar-membersecondary-api
- description: The MemberSingleOwnedMLS API from National Association of REALTORS — 1 operation(s) for membersingleownedmls.
  name: National Association of REALTORS Member Single Owned MLS API
  slug: nar-membersingleownedmls-api
- description: The Office API from National Association of REALTORS — 5 operation(s) for office.
  name: National Association of REALTORS Office API
  slug: nar-office-api
- description: The OfficeSecondary API from National Association of REALTORS — 2 operation(s) for officesecondary.
  name: National Association of REALTORS Office Secondary API
  slug: nar-officesecondary-api
artifact_total: 30
collections:
- collection_type: open
  name: M1Gateway - External
  slug: open-nar-m1-gateway-external
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/nar-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/nar-m1-gateway-external-overlay.yaml
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
  name: National Association of REALTORS MCP Server
  slug: national-association-of-realtors-mcp-server
modified: '2026-07-26'
name: National Association of REALTORS
nav: Providers
network: true
overview: 'National Association of REALTORS publishes 24 APIs on the [APIs.io](https://apis.io/) network, including Association API, Data Extract Request API, Data Extract Schedule API, and 21 more. Tagged areas include Real-Estate, United States, Industry Body, MLS, and RESO.


  National Association of REALTORS''s developer surface includes authentication, engineering blog, documentation, support, and 23 more developer resources.'
random_paper: 6
rate_limits:
- limit_count: 1
  name: Nar Rate Limits
  slug: nar-rate-limits
score:
  band: thin
  composite: 30.9
  coverage:
    artifact_dirs: 22
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 36.8
    developer_ergonomics: 35.1
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 23.7
  previous_composite: 30.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 24
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
- Real-Estate
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
