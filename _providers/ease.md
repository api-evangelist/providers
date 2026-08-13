---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.1
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ease Agentic Access
  operation_count: 37
  slug: ease-agentic-access
  summary_line: 37 operations
api_count: 2
apis:
- description: 'The public, anonymous WordPress REST API behind www.ease.com. It is not the Ease benefits administration API, but it is a real machine-readable surface and it carries the Ease Marketplace: 110 publish'
  name: Ease Content & Marketplace API
  slug: ease-content-marketplace-api
- description: The public, anonymous Atlassian Statuspage v2 API for the Ease platform, hosted at status.ease.com (page id 13zw4w6v89nk) and documented by Ease itself at https://status.ease.com/api. Eight GET endpoi
  name: Ease Status API
  slug: ease-status-api
artifact_total: 13
asyncapis:
- description: ''
  name: Ease Status Webhooks
  slug: ease-status-webhooks
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ease-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ease-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ease-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ease-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ease-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ease-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ease-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://www.employeenavigator.com/ease-platform-sunset-announcement/
- group: design
  title: ''
  type: Conformance
  url: conformance/ease-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.ease.com/product/security/sso/
- group: auth
  title: ''
  type: TrustCenter
  url: security/ease-trust-center.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ease-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ease-well-known.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ease-status-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ease-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Examples
  url: examples/ease-partners.json
- group: docs
  title: ''
  type: APIReference
  url: https://status.ease.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://help.ease.com/
- group: start
  title: ''
  type: Login
  url: https://secure.ease.com/
- group: company
  title: ''
  type: Website
  url: https://www.ease.com/
- group: company
  title: ''
  type: Blog
  url: https://www.ease.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.ease.com/blog/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ease
- group: operate
  title: ''
  type: Support
  url: https://www.ease.com/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.ease.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ease.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ease.com/pricing/
- group: auth
  title: ''
  type: Security
  url: https://www.ease.com/product/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ease.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ease.com/terms/
- group: company
  title: ''
  type: PartnerProgram
  url: https://www.ease.com/partners/join-us/
- group: other
  title: ''
  type: Marketplace
  url: https://www.ease.com/marketplace/
created: '2026-07-25'
description: 'Ease (legally Enrollease, Inc., San Francisco, with offices in Las Vegas and Omaha) is a United States benefits administration and HR platform sold through insurance brokers to small and mid-sized employers of roughly 2-250 employees. It covers online benefits enrollment, benefits and plan management, ACA reporting, onboarding and offboarding, and a partner marketplace spanning carriers, general agencies, third-party administrators, payroll providers and agency management systems. Ease is a group-benefits distribution platform rather than a risk carrier, so its lines of business are medical, dental, vision, life, AD&D, STD, LTD and voluntary/supplemental products written by its carrier partners. It was acquired by Employee Navigator in April 2023 and is now in announced end-of-life: Employee Navigator published a dated two-phase sunset on 2026-06-03 under which no new companies can be added to Ease from 2027-01-01 and the platform goes read-only, with integrations and support
  discontinued, on 2027-07-01. Its benefits API posture is partner-gated and closed: Ease publishes no public developer portal and no API reference for the product. developer.ease.com, developers.ease.com, api.ease.com and docs.ease.com all resolve through wildcard DNS to the Ease application sign-in page, and ease.com/developers, /api, /developer and /integrations return 404. The real integration surface is EaseConnect (self-service mapping of ANSI X12 EDI 834 enrollment files to carriers), EaseConnect+ (privately negotiated direct carrier data connections, which in the Principal integration include an Evidence of Insurability API and a Member Benefits API that Ease never documents publicly), marketplace API integrations with payroll and HRIS vendors such as ADP Workforce Now, ADP RUN, BambooHR, Paycor and Paylocity, and a partner portal whose data leaves by scheduled report or SFTP. Ease does however operate two real, anonymous, machine-readable read surfaces that this record captures:
  the WordPress REST API behind www.ease.com, which serves the full Ease Marketplace partner directory (110 partners, 16 partner types, 23 benefit types) alongside blog, page, event and testimonial content; and the Atlassian Statuspage v2 API on status.ease.com, which serves platform status, component health, incident history and an anonymous incident-webhook subscription. No ACORD, AL3, NGDS or IVANS reference appears anywhere on the site - Ease operates in the group-benefits ANSI X12 834 idiom, not the P&C ACORD idiom.'
examples:
- key_count: 17
  name: Ease Content Types
  slug: ease-content-types
- key_count: 2
  name: Ease Status Components
  slug: ease-status-components
- key_count: 2
  name: Ease Status Incidents
  slug: ease-status-incidents
- key_count: 2
  name: Ease Status Status
  slug: ease-status-status
- key_count: 5
  name: Ease Status Summary
  slug: ease-status-summary
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: ease-mcp.yml
  slug: ease-mcpyml
modified: '2026-07-25'
name: Ease
nav: Providers
network: true
overview: 'Ease publishes 2 APIs on the [APIs.io](https://apis.io/) network: Content & Marketplace API and Status API. Tagged areas include Insurance, United States, Employee Benefits, Benefits Administration, and Group Benefits.


  The Ease catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ease''s developer surface includes authentication, code examples, API reference, documentation, engineering blog, support, pricing, and 26 more developer resources.'
random_paper: 54
score:
  band: developing
  composite: 42.6
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 24.1
    developer_ergonomics: 36.4
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 42.1
  previous_composite: 42.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 45.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ease/refs/heads/main/screenshots/ease-2026-07-25T212704.png
security:
- kind: authentication
  name: Ease Authentication
  slug: ease-authentication
  summary_line: none/http · 2 schemes
- kind: domain-security
  name: Ease Domain Security
  slug: ease-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Ease Trust Center
  slug: ease-trust-center
  summary_line: SOC 2 Type II, HITRUST, HIPAA, GDPR, CCPA, 23 NYCRR 500 (NYDFS), NIST
slug: ease
tags:
- Insurance
- United States
- Employee Benefits
- Benefits Administration
- Group Benefits
- Health Insurance
- Insurtech
- Broker
- Enrollment
- EDI
- Payroll
- Human Resources
- Marketplace
- Status
website: https://www.ease.com/
---
