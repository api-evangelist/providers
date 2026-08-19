---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ripe Insurance Agentic Access
  operation_count: 8
  slug: ripe-insurance-agentic-access
  summary_line: 8 operations
api_count: 2
apis:
- description: The read-only Umbraco CMS Content Delivery API served anonymously from the Ripe Insurance marketing and quote site. This is platform infrastructure that ships with Umbraco, not an insurance product AP
  name: Ripe Insurance Umbraco Content Delivery API
  slug: ripe-insurance-umbraco-content-delivery-api
- description: The read-only Umbraco CMS Content Delivery API served anonymously from cycleplan.co.uk, the Ripe Insurance bike-insurance brand. Same platform infrastructure as the flagship site but running one CMS v
  name: Cycleplan Umbraco Content Delivery API
  slug: ripe-insurance-cycleplan-content-delivery-api
artifact_total: 9
collections:
- collection_type: open
  name: Umbraco Delivery API
  slug: open-ripe-insurance-cycleplan-content-delivery
- collection_type: open
  name: Umbraco Delivery API
  slug: open-ripe-insurance-umbraco-content-delivery
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ripe-insurance-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ripe-insurance-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ripe-insurance-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ripe-insurance-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ripe-insurance-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ripe-insurance-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ripe-insurance-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ripe-insurance-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ripe-insurance-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ripe-insurance-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/ripe-insurance-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ripe-insurance-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ripe-insurance-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/ripe-insurance-tool-crosswalk.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/ripe-insurance-openid-configuration.json
- group: company
  title: ''
  type: Website
  url: https://www.ripeinsurance.co.uk/
- group: company
  title: ''
  type: CorporateWebsite
  url: https://www.ripethinking.co.uk/
- group: company
  title: ''
  type: Partners
  url: https://www.ripethinking.co.uk/partner-with-us/
- group: other
  title: ''
  type: Technology
  url: https://www.ripethinking.co.uk/technology/
- group: company
  title: ''
  type: About
  url: https://www.ripeinsurance.co.uk/about/
- group: operate
  title: ''
  type: Support
  url: https://www.ripeinsurance.co.uk/help-and-support/
- group: other
  title: ''
  type: Claims
  url: https://www.ripeinsurance.co.uk/how-to-claim/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ripeinsurance.co.uk/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ripeinsurance.co.uk/privacy-policy/
- group: company
  title: ''
  type: News
  url: https://www.ripethinking.co.uk/news/
- group: company
  title: ''
  type: Blog
  url: https://www.ripeinsurance.co.uk/motorhome-insurance/blog/
- group: start
  title: ''
  type: Login
  url: https://www.ripeinsurance.co.uk/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RipeThinking
- group: company
  title: ''
  type: LinkedIn
  url: https://uk.linkedin.com/company/ripe-insurance
- group: other
  title: ''
  type: OpenIDConnectDiscovery
  url: https://www.ripeinsurance.co.uk/.well-known/openid-configuration
created: '2026-07-25'
description: Ripe Insurance Services Limited, trading as Ripe and part of Ripe Thinking Limited, is a Stockport-based United Kingdom digital Managing General Agent and specialist insurance intermediary authorised and regulated by the Financial Conduct Authority (FRN 313411). Founded in 1997 and majority-backed by Aquiline Capital Partners, Ripe underwrites and distributes niche personal and small-commercial lines direct to consumers through its own brands — Cycleplan, Golf Care, Insure4Boats, Insure4Sport and Ripe Caravans — covering caravans and motorhomes, park homes and holiday homes, photography and music equipment, valuables, shooting, golf, cycling, boats, over 400 sports, personal trainers, hair and beauty businesses, clubs and leisure organisations, and small business. It reports more than 400,000 policyholders. Ripe's API posture is honestly assessed as partner-gated with no public developer surface — there is no developer portal, no self-serve API programme, no published quote,
  bind, issue or FNOL API, and no ACORD reference anywhere on its estate. Its in-house platform is marketed as flexible and fast to integrate, but partnering is a business-development contact form on ripethinking.co.uk rather than a technical onboarding path. The only anonymously reachable, machine-readable API surface across the Ripe brand estate is the Umbraco CMS Content Delivery API that ships with its .NET content management system — read-only content and media, incidental infrastructure rather than an insurance product API. Its April 2026 Cycleplan ChatGPT app delivers real-time cycling quotes conversationally, but is a first-party consumer channel with no published API, MCP server, or spec.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: ripe-insurance-mcp.yml
  slug: ripe-insurance-mcpyml
modified: '2026-07-25'
name: Ripe Insurance
nav: Providers
network: true
overview: 'Ripe Insurance publishes 2 APIs on the [APIs.io](https://apis.io/) network: Umbraco Content Delivery API and Cycleplan Umbraco Content Delivery API. Tagged areas include Insurance, United Kingdom, Insurtech, Managing General Agent, and Specialist Insurance.


  Ripe Insurance''s developer surface includes authentication, support, product news, engineering blog, and 27 more developer resources.'
random_paper: 104
scopes:
- name: Ripe Insurance Scopes
  scope_count: 2
  slug: ripe-insurance-scopes
  summary_line: 2 scopes · authorizationCode/clientCredentials/refreshToken
score:
  band: developing
  composite: 42.2
  delta: 5.4
  facets:
    access_clarity: 57.1
    commercial_clarity: 57.1
    contract_governance: 16.7
    contract_quality: 40.6
    developer_ergonomics: 20.8
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 2.6
  previous_composite: 36.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 63.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: rising
security:
- kind: authentication
  name: Ripe Insurance Authentication
  slug: ripe-insurance-authentication
  summary_line: none/apiKey/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Ripe Insurance Domain Security
  slug: ripe-insurance-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ripe-insurance
tags:
- Insurance
- United Kingdom
- Insurtech
- Managing General Agent
- Specialist Insurance
- Personal Lines
- Small Business Insurance
- Underwriting
- Direct to Consumer
- Broker
website: https://www.ripeinsurance.co.uk/
---
