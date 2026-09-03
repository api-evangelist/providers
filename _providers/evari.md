---
access_model:
  confidence: medium
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.2
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Evari Agentic Access
  operation_count: 56
  slug: evari-agentic-access
  summary_line: 56 operations · 17 acting
api_count: 1
apis:
- baseURL: https://api.cloudstream.evari.tech/
  baseurl_source: declared
  description: The Evari Quotes microservice - the internal broker and underwriter quoting surface at /api/quotes/** plus a customer-facing mirror at /api/quotes/public/**. 49 paths, 56 operations and 70 definitions
  name: Evari Quotes API
  slug: evari-quotes-api
artifact_total: 10
collections:
- collection_type: open
  name: Evari Quotes API
  slug: open-evari-quotes-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/evari-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://evari.tech/
- group: docs
  title: ''
  type: Documentation
  url: https://evari.tech/help-center/
- group: start
  title: ''
  type: GettingStarted
  url: https://evari.tech/help-center/categories/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://evari.tech/help-center/contact/
- group: company
  title: ''
  type: Blog
  url: https://evari.tech/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://evari.tech/blog/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/myevari
- group: commercial
  title: ''
  type: Pricing
  url: https://evari.tech/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/evari-plans.yml
- group: start
  title: ''
  type: SignUp
  url: https://quiva.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://evari.tech/legal#terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://evari.tech/legal#privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://evari.tech/trust
- group: auth
  title: ''
  type: TrustCenter
  url: security/evari-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://evari.tech/trust
- group: auth
  title: ''
  type: Security
  url: https://evari.tech/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/evari-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/evari-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/evari-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/evari-domain-security.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/evari-quotes-api-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/evari-contracts-types.json
- group: build
  title: ''
  type: Packages
  url: packages/evari-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/evari-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/evari-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/evari-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/evari-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/evari-lifecycle.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/evari-agentic-access.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/evari-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/evari-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/evari-quotes-api-overlay.yaml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/evari/
created: '2026-07-25'
description: Evari is an insurance technology company founded in Sydney by Daniel Fogarty (former CEO of Zurich Australia and New Zealand), Robert Jeffery and Brack Norris, and now operating as Evari Services UK Ltd. It launched as a digital small-business and trades insurance brand at evari.insure, a Lloyd's coverholder with direct and partner distribution, then moved upstream into core systems with CloudStream, a cloud-native policy administration platform covering quote, bind and issue through endorsement, renewal and cancellation, broker and MGA portals, appetite and eligibility rules, commission tracking and policyholder self-service. Its current positioning is insurance AI operations for brokers, MGAs and insurers, delivered as 30-day assistant deployment sprints powered by the third-party QuivaWorks platform. Evari publishes no developer portal and no API reference, and every running API host is tenant-scoped and closed - api.cloudstream.evari.tech returns 404 unauthenticated, api.envest.evari.tech
  returns 502, and the customer and admin applications are login walls. One real first-party contract does exist off-portal - Evari published its Quotes microservice to npm as evari-quotes-api, and that tarball ships a generated Swagger 2.0 document of 49 paths and 56 operations plus a draft-07 JSON Schema set of 369 definitions, both harvested here. Evari is otherwise a consumer of other vendors' APIs, integrating into Socotra, Vertafore AMS360 and Sagitta, Applied Epic and Guidewire read access, and no ACORD, AL3 or IVANS reference appears anywhere on its site, in its help centre or in its data model.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
json_schemas:
- name: Evari Contracts Types
  property_count: 0
  slug: evari-contracts-types
layout: provider
mcp_servers:
- description: ''
  name: Evari MCP Server
  slug: evari-mcp-server
modified: '2026-07-25'
name: Evari
nav: Providers
network: true
overview: 'Evari publishes 1 API on the [APIs.io](https://apis.io/) network: Quotes API. Tagged areas include Insurance, Australia, Insurtech, Policy Administration, and Core Systems.


  Evari''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, signup flow, authentication, and 28 more developer resources.'
plans:
- name: Evari Plans
  plan_count: 6
  slug: evari-plans
random_paper: 10
score:
  band: developing
  composite: 50.9
  coverage:
    artifact_dirs: 20
    catalog_gap: 60.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 78.9
    commercial_clarity: 78.9
    contract_governance: 18.2
    contract_quality: 44.2
    developer_ergonomics: 42.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 50.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 54.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/evari/refs/heads/main/screenshots/evari-2026-07-25T213710.png
security:
- kind: authentication
  name: Evari Authentication
  slug: evari-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Evari Domain Security
  slug: evari-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Evari Vulnerability Disclosure
  slug: evari-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Evari Trust Center
  slug: evari-trust-center
  summary_line: ISO 27001, GDPR
slug: evari
tags:
- Insurance
- Australia
- Insurtech
- Policy Administration
- Core Systems
- Property and Casualty
- Underwriting
- Claims
- Brokers
- MGA
- Artificial Intelligence
- Quoting
- Endorsements
website: https://evari.tech/
---
