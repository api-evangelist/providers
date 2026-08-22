---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-08-19'
api_count: 8
apis:
- description: A first-party Model Context Protocol tool manifest published by Fullpath for AI assistants. Thirteen tools with real JSON Schema inputSchemas covering consent management, shoppers, audiences, tasks, l
  name: Fullpath MCP Tools
  slug: fullpath-mcp-tools
- description: Operations related to activities
  name: AutoLeadStar Activities API
  slug: autoleadstar-activities-api
- description: Operations related to appointments
  name: AutoLeadStar Appointments API
  slug: autoleadstar-appointments-api
- description: Operations related to audiences
  name: AutoLeadStar Audiences API
  slug: autoleadstar-audiences-api
- description: Vendor Consent Management API for listing integrated dealers and reading/writing communication consent. Defaults to `https://fullpath.com/api/v2/external/consent-management`.
  name: AutoLeadStar Consents API
  slug: autoleadstar-consents-api
- description: Operations related to leads
  name: AutoLeadStar Leads API
  slug: autoleadstar-leads-api
- description: Operations related to shoppers
  name: AutoLeadStar Shoppers API
  slug: autoleadstar-shoppers-api
- description: Operations related to tasks
  name: AutoLeadStar Tasks API
  slug: autoleadstar-tasks-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Autoleadstar Activities API
  slug: open-autoleadstar-activities-api
- collection_type: open
  name: Autoleadstar Appointments API
  slug: open-autoleadstar-appointments-api
- collection_type: open
  name: Autoleadstar Audiences API
  slug: open-autoleadstar-audiences-api
- collection_type: open
  name: Autoleadstar Consents API
  slug: open-autoleadstar-consents-api
- collection_type: open
  name: Autoleadstar Leads API
  slug: open-autoleadstar-leads-api
- collection_type: open
  name: Autoleadstar Shoppers API
  slug: open-autoleadstar-shoppers-api
- collection_type: open
  name: Autoleadstar Tasks API
  slug: open-autoleadstar-tasks-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/autoleadstar-fullpath-api-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/autoleadstar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fullpath.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.fullpath.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.fullpath.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.fullpath.com/
- group: company
  title: ''
  type: Blog
  url: https://www.fullpath.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://fullpath.zendesk.com/hc/en-us
- group: start
  title: ''
  type: SignUp
  url: https://app.fullpath.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fullpath.com/legal-and-trust/?nav=websiteterms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fullpath.com/legal-and-trust/?nav=privacypolicy
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.fullpath.com/feature-releases/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/autoleadstar-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/autoleadstar-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/autoleadstar-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/autoleadstar-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.fullpath.com/vulnerability-disclosure-policy
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/autoleadstar-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/autoleadstar-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.fullpath.com/legal-and-trust/
- group: design
  title: ''
  type: Conformance
  url: conformance/autoleadstar-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/autoleadstar-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/autoleadstar-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/autoleadstar-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/autoleadstar-lifecycle.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://forgeglobal.com/autoleadstar_stock/
created: '2026-08-06'
description: AutoLeadStar is an automotive marketing technology company founded in 2015 in Jerusalem, Israel, that rebranded as Fullpath in March 2023 after raising a $40M Series C. It builds an enhanced Customer Data Platform (CDP) and AI ecosystem for franchise car dealerships, unifying first-party data from the dealership CRM, DMS, website, inventory feed and advertising accounts into a single shopper profile, then activating it through digital advertising, VIN-specific campaigns, equity mining, email/SMS audience activation, website personalization and an AI chat agent. The company opened a public API for the platform in November 2022 and today publishes a Scalar-rendered OpenAPI 3.0 reference at developers.fullpath.com covering shoppers, audiences, leads, tasks, appointments, activities and a vendor Consent Management API, alongside a downloadable Model Context Protocol tool manifest. Fullpath reports more than 2,000 dealership clients across North America and 200+ pre-built integrations,
  and was acquired by Cox Automotive.
image: https://developers.fullpath.com/fullpath-logo.png
layout: provider
mcp_servers:
- description: ''
  name: autoleadstar-mcp.yml
  slug: autoleadstar-mcpyml
modified: '2026-08-14'
name: AutoLeadStar
nav: Providers
network: true
overview: 'AutoLeadStar publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Appointments API, Audiences API, and 4 more. Tagged areas include Company, Automotive, Customer Data Platform, Marketing Automation, and Dealerships.


  AutoLeadStar''s developer surface includes documentation, API reference, engineering blog, support, signup flow, changelog, and 21 more developer resources.'
plans:
- name: Autoleadstar Plans Pricing
  plan_count: 0
  slug: autoleadstar-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Autoleadstar Rate Limits
  slug: autoleadstar-rate-limits
score:
  band: developing
  composite: 50.0
  delta: 1.1
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 30.3
    contract_quality: 60.0
    developer_ergonomics: 35.1
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 47.4
  previous_composite: 48.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/autoleadstar/refs/heads/main/screenshots/autoleadstar-2026-08-07T161958.png
security:
- kind: authentication
  name: Autoleadstar Authentication
  slug: autoleadstar-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Autoleadstar Domain Security
  slug: autoleadstar-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Autoleadstar Vulnerability Disclosure
  slug: autoleadstar-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Autoleadstar Trust Center
  slug: autoleadstar-trust-center
  summary_line: ISO/IEC 27001, ISO/IEC 42001
slug: autoleadstar
tags:
- Company
- Automotive
- Customer Data Platform
- Marketing Automation
- Dealerships
- Advertising
- Artificial Intelligence
- Consent Management
- CRM
- Israel
website: https://www.fullpath.com/
---
