---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.6
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ease Agentic Access
  operation_count: 37
  slug: ease-agentic-access
  summary_line: 37 operations
api_count: 2
apis:
- description: 'Self-describing metadata: registered content types, taxonomies and post statuses.'
  name: Ease Discovery API
  slug: ease-discovery-api
- description: Ease in-person and virtual events, and their categories.
  name: Ease Events API
  slug: ease-events-api
- description: Unresolved and historical incidents, each composed of dated incident updates.
  name: Ease Incidents API
  slug: ease-incidents-api
- description: Upcoming, active and historical scheduled maintenance windows.
  name: Ease Maintenance API
  slug: ease-maintenance-api
- description: 'The Ease Marketplace partner directory: carriers, general agencies, third-party administrators, payroll providers and agency-management vendors, plus the partner_types and benefit_types taxonomies use'
  name: Ease Marketplace API
  slug: ease-marketplace-api
- description: Images and files in the Ease media library.
  name: Ease Media API
  slug: ease-media-api
- description: oEmbed representation of an ease.com URL.
  name: Ease O Embed API
  slug: ease-oembed-api
- description: Marketing and product pages on www.ease.com.
  name: Ease Pages API
  slug: ease-pages-api
- description: The Ease blog.
  name: Ease Posts API
  slug: ease-posts-api
- description: Cross-content-type search over published site content.
  name: Ease Search API
  slug: ease-search-api
- description: Rollup status indicator and per-component status for the Ease platform.
  name: Ease Status API
  slug: ease-status-api
- description: Blog categories and tags.
  name: Ease Taxonomy API
  slug: ease-taxonomy-api
- description: Published customer testimonials.
  name: Ease Testimonials API
  slug: ease-testimonials-api
artifact_total: 27
asyncapis:
- description: ''
  name: Ease Status Webhooks
  slug: ease-status-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-ease-content-wp-routes-original
- collection_type: open
  name: Ease Content & Marketplace API
  slug: open-ease-content
- collection_type: open
  name: Ease Status API
  slug: open-ease-status
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/ease-content-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ease-status-overlay.yaml
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
  name: Ease MCP Server
  slug: ease-mcp-server
modified: '2026-07-25'
name: Ease
nav: Providers
network: true
overview: 'Ease publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Discovery API, Events API, Incidents API, and 10 more. Tagged areas include Insurance, United States, Employee Benefits, Benefits Administration, and Group Benefits.


  The Ease catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ease''s developer surface includes authentication, code examples, API reference, documentation, engineering blog, support, pricing, and 28 more developer resources.'
random_paper: 15
score:
  band: developing
  composite: 41.8
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 25.1
    developer_ergonomics: 37.5
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 42.4
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
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
- Brokers
- Enrollment
- EDI
- Payroll
- Human Resources
- Marketplace
- Status
website: https://www.ease.com/
---
