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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Arcadia Power Agentic Access
  operation_count: 26
  slug: arcadia-power-agentic-access
  summary_line: 26 operations · 6 acting
api_count: 15
apis:
- description: Arcadia Connect is a hosted credential-collection web experience that handles utility account onboarding — credential capture, MFA flows, one-time passcodes, and credential refresh — without requiring
  name: Arcadia Connect API
  slug: arcadia-connect-api
- description: Arcadia Signal provides utility tariff and energy rate data and calculations for use in cost-benefit analyses, bill audits, project forecasting, and financial modeling. Signal powers the Tariff & Ener
  name: Arcadia Signal API
  slug: arcadia-signal-api
- description: List, retrieve, and resend webhooks for asynchronous Plug platform events including statement availability, meter activation, interval data readiness, and credential lifecycle changes. Arcadia recomme
  name: Arcadia Webhooks API
  slug: arcadia-webhooks-api
- description: 'The legacy Utility Cloud REST API — predecessor to the Plug API — still documented for existing integrations. New integrations should use the Plug API; the Utility Cloud version remains available for '
  name: Arcadia Utility Cloud API (Legacy)
  slug: arcadia-utility-cloud-api
- description: Utility accounts discovered for a credential.
  name: Arcadia Accounts API
  slug: arcadia-power-accounts-api
- description: Utility-login credentials used to pull data on behalf of customers.
  name: Arcadia Credentials API
  slug: arcadia-power-credentials-api
- description: Source documents (PDFs, etc.) for statements and other artifacts.
  name: Arcadia Files API
  slug: arcadia-power-files-api
- description: Time-series consumption data, typically 15-minute resolution.
  name: Arcadia Intervals API
  slug: arcadia-power-intervals-api
- description: Individual measurement devices associated with accounts and sites.
  name: Arcadia Meters API
  slug: arcadia-power-meters-api
- description: Access token issuance.
  name: Arcadia OAuth API
  slug: arcadia-power-oauth-api
- description: Top-level organization resource.
  name: Arcadia Organizations API
  slug: arcadia-power-organizations-api
- description: Utility providers supported by the platform.
  name: Arcadia Providers API
  slug: arcadia-power-providers-api
- description: Physical service locations grouping meters and accounts.
  name: Arcadia Sites API
  slug: arcadia-power-sites-api
- description: Utility bills / statements pulled from the provider.
  name: Arcadia Statements API
  slug: arcadia-power-statements-api
- description: Asynchronous events for statement, meter, and credential lifecycle.
  name: Arcadia Webhooks API
  slug: arcadia-power-webhooks-api
artifact_total: 57
collections:
- collection_type: postman
  name: Arcadia Plug Accounts API
  slug: postman-arcadia-power-accounts-api
- collection_type: postman
  name: Arcadia Plug Accounts Credentials API
  slug: postman-arcadia-power-credentials-api
- collection_type: postman
  name: Arcadia Plug Accounts Files API
  slug: postman-arcadia-power-files-api
- collection_type: postman
  name: Arcadia Plug Accounts Intervals API
  slug: postman-arcadia-power-intervals-api
- collection_type: postman
  name: Arcadia Plug Accounts Meters API
  slug: postman-arcadia-power-meters-api
- collection_type: postman
  name: Arcadia Plug Accounts OAuth API
  slug: postman-arcadia-power-oauth-api
- collection_type: postman
  name: Arcadia Plug Accounts Organizations API
  slug: postman-arcadia-power-organizations-api
- collection_type: postman
  name: Arcadia Plug Accounts Providers API
  slug: postman-arcadia-power-providers-api
- collection_type: postman
  name: Arcadia Plug Accounts Sites API
  slug: postman-arcadia-power-sites-api
- collection_type: postman
  name: Arcadia Plug Accounts Statements API
  slug: postman-arcadia-power-statements-api
- collection_type: postman
  name: Arcadia Plug Accounts Webhooks API
  slug: postman-arcadia-power-webhooks-api
- collection_type: open
  name: Arcadia Plug API
  slug: open-arcadia-plug-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/arcadia/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/arcadia-power-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/arcadia-power-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/arcadia-power-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arcadia-power-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/arcadia-power-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.arcadia.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.arcadia.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.arcadia.com/arc
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.arcadia.com/docs/api-quick-start-guide
- group: docs
  title: ''
  type: Documentation
  url: https://docs.arcadia.com/docs/arcadia-data-model
- group: start
  title: ''
  type: Signup
  url: https://dashboard.arcadia.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/arcadiapower
- group: company
  title: ''
  type: Blog
  url: https://www.arcadia.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.arcadia.com/changelog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.arcadia.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.arcadia.com/terms-of-service
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/arcadiapower
- group: company
  title: ''
  type: Press
  url: https://www.arcadia.com/press
- group: docs
  title: ''
  type: Documentation
  url: https://docs.arcadia.com/reference/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://docs.arcadia.com/v2022-12-21-Signal/docs/quick-start
- group: docs
  title: ''
  type: Documentation
  url: https://docs.arcadia.com/docs/connect-guide
- group: docs
  title: ''
  type: Documentation
  url: https://docs.arcadia.com/reference/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://docs.arcadia.com/llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/arcadia-power-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/arcadia-power-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/arcadia-power-finops.yml
created: '2026-05-25T00:00:00.000Z'
description: Arcadia is a clean-energy access and energy-intelligence company that operates Arc, a utility data platform giving developers programmatic access to utility bills, statements, meters, interval (15-minute) usage data, tariff rates, and provider metadata across thousands of US and international utilities. Arc combines the Plug API for utility data, Arcadia Connect for hosted credential collection and MFA, Signal for tariff and rate calculations, and webhooks for asynchronous events. Arcadia powers solar and storage modeling, EV charging, energy management, property management, and carbon accounting for customers including Ford, EVgo, Enphase, Oracle, UPS, Conagra, Penske, and ~25% of the Fortune 500. In April 2026 Arcadia acquired ENGIE Impact, adding utility bill management, energy procurement advisory, and sustainability reporting capabilities.
features:
- Arc — unified utility data platform for bills, meters, intervals, providers, and sites
- Plug API for programmatic access to statements, meters, interval data, accounts, sites, providers, and files
- Arcadia Connect hosted credential UI handles utility logins, MFA, and one-time passcodes without partners storing utility credentials
- Signal API for tariff calculations, energy rates, and rate-based cost-benefit analysis
- 15-minute interval data for electric meters with bulk and on-demand delivery
- Coverage across thousands of US utilities plus international expansion
- OAuth 2.0 client-credentials authentication with one-hour bearer tokens
- Arcadia-Version request header for date-pinned API versioning (default 2024-02-21)
- Sandbox mode for safe end-to-end testing of credentials, statements, and intervals
- Webhook events for statement availability, meter activation, interval readiness, credential MFA, and lifecycle changes
- CSV download requests and bulk export streaming for large statement and interval pulls
- Arcadia Data Model normalizes provider tariffs, charges, taxes, and usage into a unified shape
- Enterprise Utility Bill Management, Energy Procurement Advisory, and Sustainability Reporting solutions
- ENGIE Impact acquired (April 2026) — sustainability advising, utility bill management, and procurement consultancy now under Arcadia
- Trusted by Ford, EVgo, Enphase, Oracle, UPS, Conagra, Penske, Iron Mountain, Intuit, and 25% of the Fortune 500
- Manages nearly $100B in utility spend and 580 million MWh of annual electricity usage post-ENGIE Impact
- Built for solar & storage, EV charging, energy management, property management, and carbon accounting integrators
finops:
- name: Arcadia Power Finops
  service_category: ''
  slug: arcadia-power-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/arcadia-power.png
json_schemas:
- name: Arcadia Interval Series
  property_count: 7
  slug: arcadia-interval
- name: Arcadia Meter
  property_count: 15
  slug: arcadia-meter
- name: Arcadia Statement
  property_count: 19
  slug: arcadia-statement
jsonld:
- class_count: 30
  name: Arcadia Power Context
  property_count: 8
  slug: arcadia-power-context
layout: provider
modified: '2026-05-25'
name: Arcadia
nav: Providers
network: true
overview: 'Arcadia publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Credentials API, Files API, and 8 more. Tagged areas include Energy, Clean Energy, Utility Data, Climate, and Sustainability.


  The Arcadia catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Arcadia''s developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, engineering blog, changelog, and 20 more developer resources.'
plans:
- name: Arcadia Power Plans Pricing
  plan_count: 4
  slug: arcadia-power-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 5
  name: Arcadia Power Rate Limits
  slug: arcadia-power-rate-limits
rules:
- name: Arcadia API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: arcadia-power-jsonschema-spectral-rules
score:
  band: strong
  composite: 59.1
  delta: 0.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 71.4
    developer_ergonomics: 45.7
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 59.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 48.6
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/arcadia-power/refs/heads/main/screenshots/arcadia-power-2026-06-20T172402.png
security:
- kind: authentication
  name: Arcadia Power Authentication
  slug: arcadia-power-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Arcadia Power Domain Security
  slug: arcadia-power-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Arcadia Power Vulnerability Disclosure
  slug: arcadia-power-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Arcadia Power Trust Center
  slug: arcadia-power-trust-center
  summary_line: SOC 2, ISO 27001
slug: arcadia-power
tags:
- Energy
- Clean Energy
- Utility Data
- Climate
- Sustainability
- Carbon Accounting
- Solar
- Storage
- EV Charging
- Decarbonization
- Energy Intelligence
website: https://www.arcadia.com
---
